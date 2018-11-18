//
//  LibraryPage.swift
//  eMello
//
//  Created by eMelloTeam on 2018/6/28.
//  Copyright © 2018 testing. All rights reserved.
//

import UIKit

/* Library Page View refers to the Library/Bookshelf View.
 Individual cells are controlled by the other file, "LibrarypageCollectionViewCell.swift"
 */

class LibrarypageViewController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource, UICollectionViewDelegateFlowLayout {
    
    //MARK: Properties
    var model = BookModel()
    var bookArray = [Book]()
    var libraryPage = LibrarypageCollectionViewCell()
    var BGM:Bool?
    //Variables used to decide whether to load tutorial or not
    var TutorialCounter = 0
    var MelodyTutorialActive = false
    var melodyCounter = 0
    //Outlets
    @IBOutlet weak var MelodyTutorialLeading: NSLayoutConstraint!
    @IBOutlet weak var bookCollectionView: UICollectionView!
    @IBOutlet weak var topBlocker: UIView!
    @IBOutlet weak var botBlocker: UIView!
    @IBOutlet weak var rightBlocker: UIView!
    @IBOutlet weak var MelodyTutorial: UIView!
    @IBOutlet weak var MelodyImage: UIImageView!
    @IBOutlet weak var SpeechLabel: UILabel!
    
    //MARK: TutorialActions
    //The following few actions pertain to the Tutorial.
    
    //This button at the top-right starts the tutorial sequence manually.
    @IBAction func melodyButton(_ sender: UIButton) {
        print("Tutorial was tapped. Tutorial counter: \(TutorialCounter).")
        MelodyTutorialActive = true
        // Load Melody tutorial
        print("Load tutorial")
        MelodyTutorial.isHidden = false
        TutorialCounter += 1
    }
    
    //This button at the top-right quits the Tutorial prematurely.
    @IBAction func QuitTutorial(_ sender: UIButton) {

        MelodyTutorialActive = false
        MelodyTutorial.isHidden = true
        
        //Resets Melody to original settings
        MelodyTutorial.backgroundColor = UIColor(white: 0, alpha: 0.5)
        topBlocker.alpha = 0
        rightBlocker.alpha = 0
        botBlocker.alpha = 0
        MelodyImage.image = UIImage(named: "melRightSmile")
        SpeechLabel.text = "Hello, I'm Melody! Tap anywhere to continue!"
        MelodyTutorialLeading.constant = 0
        
        //So tutorial will not load unless pressed
        TutorialCounter += 1
        
        //Resets the tutorial counter to 0
        //Tutorial will start from the first case
        melodyCounter = 0
    }
    
    //The following function is called when the user taps the screen during the tutorial.
    @IBAction func MelodyNext(_ sender: Any) {

        switch melodyCounter{
        
        case 0:
            MelodyImage.image = UIImage(named: "melExcite")
            SpeechLabel.text = "Welcome to eMello, the world of musical books."
            melodyCounter += 1
            TutorialCounter += 1
            
        case 1:
            MelodyImage.image = UIImage(named: "melNorm")
            SpeechLabel.text = "Let me show you around!"
            melodyCounter += 1
            
        case 2:
            MelodyTutorialLeading.constant = 300
            MelodyTutorial.backgroundColor = UIColor(white: 0, alpha: 0)
            topBlocker.alpha = 0.5
            rightBlocker.alpha = 0.5
            botBlocker.alpha = 0.5
            MelodyImage.image = UIImage(named: "melLeft")
            SpeechLabel.text = "Let's start with \"Finding a Friend\"! Tap on the book to open it."
            melodyCounter += 1
            
        default:
            print("No more tutorial")
        }
    }
    
    //MARK: BookshelfFunctions
    
    //Updating Librarypage
    func updatingLibrary(_ array: [Book]) -> [Book] {
        if array.count != 0 {
            return array
        }
        else {
            let newArray = model.loadSampleBooks()
            return newArray
        }
    }
    
    //MARK: Navigation
    
    //Go to Home page
    @IBAction func goToHome(_ sender: Any) {
        
        let homePage = self.storyboard?.instantiateViewController(withIdentifier: "HomePage") as! HomeViewController
        
        //Store list of books in home bookArray
        homePage.bookArray = bookArray
        
        print("HomePage now has bookArray")
        print(homePage.bookArray)
        
        //BGM Settings
        homePage.BGM = BGM!
        
        //Tutorial Settings
        homePage.TutorialCounter = TutorialCounter
        print("Tutorial counter: \(TutorialCounter)")
        
        print("Going to Home")
        self.present(homePage, animated: true, completion: nil)
    }

    //MARK: -UICollectionView Protocol Methods
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return bookArray.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        
        // Get a bookcollectionviewcell object
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "bookCell", for: indexPath) as! LibrarypageCollectionViewCell
        
        // Get the book that the collection view is trying to display
        let book = bookArray[indexPath.row]
        
        // Set that book for the cell
        cell.setBook(book)
        
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        
        //Define what story to go to

        //This occurs When add books is clicked
        if indexPath.row == (bookArray.count - 1) {
            //Bring user to uploading page
            print("Add books was tapped")
            
            let uploadPage = self.storyboard?.instantiateViewController(withIdentifier: "Uploadpage") as! UploadpageViewController
            
            //Update bookArray in Upload page
            uploadPage.bookArray = bookArray
            print("Upoad page is updated from Library page")
            print("Bookarray in Upload: \(uploadPage.bookArray)")
            
            //BGM Settings
            uploadPage.BGM = BGM!
            
            //Tutorial Settings
            uploadPage.TutorialCounter = TutorialCounter
            print("Tutorial counter: \(TutorialCounter)")
            
            print("Going to Upload page")
            self.present(uploadPage, animated: true, completion: nil)
            
        }
        
        //This occurs when other books are clicked
        else {
            if MelodyTutorialActive {
                //Go to story tutorial
                print("Going to page 1 of mermaid book")
                
                let storybook = self.storyboard?.instantiateViewController(withIdentifier: "Storybook") as! StorybookViewController
                
                //Store the index of the book that was click to update it later
                storybook.selectedIndex = indexPath.row
                
                //Store the original bookArray to update library later
                storybook.bookArray = bookArray
                
                //Store counter of book before going to tutorial
                storybook.originalpage = bookArray[indexPath.row].counter
                print("original page: \(storybook.originalpage)")
                
                //Change counter of book so tutorial will start from page 1
                bookArray[indexPath.row].counter = 0
                
                //Book in storybook should be tutorial book that was clicked with counter 0
                storybook.readingNow = bookArray[indexPath.row]
                
                //Check the counter of books
                print("Changed book counter: \(bookArray[indexPath.row].counter)")
                print("original page: \(storybook.originalpage)")
                
                //BGM Settings
                storybook.BGM = BGM!
                
                //Tutorial Settings
                storybook.MelodyTutorialActive = MelodyTutorialActive
                storybook.TutorialCounter = TutorialCounter
                print("Tutorial counter: \(TutorialCounter)")
                print("Going to Storybook")
                self.present(storybook, animated: true, completion: nil)
                
            }
            
            else{
                // Go to the story
                print("\(String(describing: bookArray[indexPath.row].name)) was clicked")
                let storybook = self.storyboard?.instantiateViewController(withIdentifier: "Storybook") as! StorybookViewController
                
                //Update ViwController with storybook properties
                storybook.readingNow = bookArray[indexPath.row]
                
                //Store the index of the book that was click to update it later
                storybook.selectedIndex = indexPath.row
                
                //Store the original bookArray to update library later
                storybook.bookArray = bookArray
                
                //BGM Settings
                storybook.BGM = BGM!
                
                //Tutorial Settings
                storybook.TutorialCounter = TutorialCounter
                print("Tutorial counter: \(TutorialCounter)")
                
                print("Going to Storybook")
                self.present(storybook, animated: true, completion: nil)
            }
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Tutorial will be hidden by default
        if TutorialCounter == 0{
            print("First time opening application")
            MelodyTutorial.isHidden = false
            print("Tutorial will now load")
            MelodyTutorialActive = true
        }
        else{
            print("Tutorial count: \(TutorialCounter)")
            MelodyTutorial.isHidden = true
            print("Tutorial will not load")
        }
        
        print("Entering Library page")
        print("Default BGM in Library page is \(BGM!)")
        
        bookCollectionView.delegate = self
        bookCollectionView.dataSource = self
        bookArray = updatingLibrary(bookArray)
        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
