//
//  UploadpageViewController.swift
//  eMello
//
//  Created by eMelloTeam on 2018/7/18.
//  Copyright © 2018 testing. All rights reserved.
//
 
import UIKit
import MobileCoreServices

/* This class deals with the Upload Function in the Library/Bookshelf.
 This upload function will access the user's iCloud Drive, takes a .epub file and sends it to our server.
 Our server will run the Watson Tone Analyser and assign a BGM to each page.
 Our server will also identify difficult words and provide them with pop-ups containing their meanings.
 The server will then send the new file back to the user's app, in the form of a book in the Library/Bookshelf page.
 */

class UploadpageViewController: UIViewController, UIDocumentPickerDelegate, UINavigationControllerDelegate {
    
    //MARK: Properties
    var bookArray = [Book]()
    var BGM:Bool?
    var TutorialCounter = 0
    
    @IBOutlet weak var EbookButton: UIButton!
    //Outlets of popup
    @IBOutlet weak var notAvailablePopup: UILabel!
    @IBOutlet weak var closePopupButton: UIButton!
    
    //MARK: To access iCloud Drive
    
    //Directly goes to iCloud to look for files
    @IBAction func selectBook(_ sender: UIButton) {
        print("Choose Ebook was pressed")
        
        //Code now shows popup that tells user that our sever is not working at the moment
        notAvailablePopup.isHidden = false
        closePopupButton.isHidden = false
        
        //Do not delete this comment
        /*
         let importMenu = UIDocumentPickerViewController( documentTypes: [String(kUTTypeElectronicPublication)], in: .import)
         importMenu.delegate = self
         importMenu.modalPresentationStyle = .formSheet
         self.present(importMenu, animated: true, completion: nil)
         */
    }
    
    //Function to choose book
    func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentsAt urls: [URL]) {
        let myURL = urls as [URL]
        print("Import result: \(myURL)")
        let EbookName = findingEbookName(myURL[0])
        print("Name of Ebook: \(EbookName)")
        EbookButton.setTitle(EbookName, for: UIControlState.normal)
        EbookButton.titleLabel?.textAlignment = NSTextAlignment.center
    }
    
    func findingEbookName(_ file:URL) -> String {
        var URLarray = [String]()
        var URLstring = file.absoluteString
        
        URLarray = URLstring.components(separatedBy: "/")
        //print(URLarray)
        URLstring = URLarray[URLarray.count - 1]
        //print(URLstring)
        URLarray = URLstring.components(separatedBy: ".")
        //print(URLarray)
        URLstring = URLarray[0]
        let fileName = URLstring.replacingOccurrences(of: "%20", with: " ")
        
        return fileName
    }
    
    func documentMenu(_ documentMenu: UIDocumentMenuViewController, didPickDocumentPicker documentPicker: UIDocumentPickerViewController) {
        
        documentPicker.delegate = self
        present( documentPicker, animated: true, completion: nil)
    }
    
    //MARK: Navigation
    
    //Now it directly returns to Library page
    func documentPickerWasCancelled(_ controller: UIDocumentPickerViewController) {
        print("Document picker was cancelled")
        dismiss(animated: true, completion: nil)
        // it dismiss the document picker view controller
        // but it brings user back to library page
        // Default BGM and bookarray was not affected
    }
    


    //This is a function to upload the .epub book that was picked to our server
    //It would run when the upload button is clicked
    
    func goToServer(){
        //1. Upload .epub book to server
        
        //2. Server will read the .epub and return a file containing the edited .html of book
        
    }
    
    
    //This function connects .epub book and the server
    @IBAction func uploadButton(_ sender: UIButton) {
        
        //Code now shows popup that tells user that our sever is not working at the moment
        notAvailablePopup.isHidden = false
        closePopupButton.isHidden = false
        
        //Ideally our server will give the nessary infomation of the book
        //this code would read the infomation and put the new book in the library
        
        //Continue from 'goToServer'
        //3. Open the file
        
        //4. Find and read 'Book info.txt'
        //   Book info.txt contains the name of the book and the number of pages
        //   Also contains the title of the song attached to each page
        
        //5. Contents will be used to initialise variables in the Book class
        
        //6. Place book into bookshelf
        /*
         bookArray.insert(newbook, at: (bookArray.count - 1)) // insert newbook just before addbook
         print("Bookarray is updated. Bookarray: \(bookArray
         */
        
        //7. Go back to Library/ Booksehlf page
        /*
         print("Going back to Library with newbook")
         goToLibrary()
         */
        
    }
    
    //Close notAvailablePopup
    @IBAction func closePopup(_ sender: UIButton) {
        notAvailablePopup.isHidden = true
        closePopupButton.isHidden = true
    }
    
    //MARK: Navigation
    
    //Cancel and return to LibraryPage
    @IBAction func cancelButton(_ sender: UIButton) {
        goToLibrary()
    }
    
    func goToLibrary(){
        let libraryPage = self.storyboard?.instantiateViewController(withIdentifier: "Librarypage") as! LibrarypageViewController
        
        //Update bookArray in Librarypage
        libraryPage.bookArray = bookArray
        print("Library page is updated from Upload page")
        print("Bookarray in Library: \(libraryPage.bookArray)")
        
        //BGM Settings
        libraryPage.BGM = BGM
        
        //Tutorial Settings
        libraryPage.TutorialCounter = TutorialCounter
        print("Tutorial counter: \(TutorialCounter)")
        
        print("Going to Library")
        self.present(libraryPage, animated: true, completion: nil)
    }
    
    //MARK: Initialization
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //Check if book array is transfered
        print("Bookarry in Upload page is \(bookArray)")
        
        //Check if status of BGM is transfered
        print("Default BGM in Upload page is \(BGM!)")
        
        //Hide popup first
        notAvailablePopup.isHidden = true
        closePopupButton.isHidden = true

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
