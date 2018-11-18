//
//  ViewController.swift
//  eMello
//
//  Created by eMelloTeam on 2018/6/26.
//  Copyright © 2018 testing. All rights reserved.
//

import UIKit
import WebKit
import AVFoundation

/* This class controls everything that happens when you are inside a storybook
 */

class StorybookViewController: UIViewController {
    
    //MARK: StorybookProperties
    var audioPlayer = AVAudioPlayer()
    var BGM:Bool?
    var pageBGM:Bool?
    var readingNow = Book()
    var selectedIndex = Int()
    var bookArray = [Book]()
    
    //MARK: TutorialProperties
    var melodyCounter = 0
    var TutorialCounter = 0
    var MelodyTutorialActive = false
    var originalpage = Int()
    @IBOutlet weak var pageNumber: UILabel!
    @IBOutlet weak var htmlCode: WKWebView!
    @IBOutlet weak var MelodyImage: UIImageView!
    @IBOutlet weak var SpeechLabel: UILabel!
    @IBOutlet weak var MelodyTutorial: UIView!
    @IBOutlet weak var bannerBlack: UIView!
    @IBOutlet weak var SwipePrompt: UIImageView!
    @IBOutlet weak var TapPrompt: UIImageView!
    @IBOutlet weak var Popup: UIImageView!
    @IBOutlet weak var xPopup: UIButton!
    @IBOutlet weak var highlightWord: UIView!
    @IBOutlet weak var swipePromptArrow: UIImageView!
    @IBOutlet weak var libPromptArrow: UIImageView!
    @IBOutlet weak var topBlocker: UIView!
    @IBOutlet weak var botBlocker: UIView!
    @IBOutlet weak var rightBlocker: UIView!
    @IBOutlet weak var leftBlocker: UIView!
    
    //MARK: Constraints
    @IBOutlet weak var HTMLTrailing: NSLayoutConstraint!
    @IBOutlet weak var HTMLLeading: NSLayoutConstraint!
    @IBOutlet weak var SwipePromptTrailing: NSLayoutConstraint!
    @IBOutlet weak var SwipePromptLeading: NSLayoutConstraint!
    @IBOutlet weak var TapPromptTop: NSLayoutConstraint!
    @IBOutlet weak var LibPromptLeading: NSLayoutConstraint!
    @IBOutlet weak var MelodyBubbleBot: NSLayoutConstraint!
    
    //MARK: Tutorial Functions
    
    //This function runs when you tap during the tutorial.
    @IBAction func TutorialViewTap(_ sender: UITapGestureRecognizer) {
        switch melodyCounter{
            
        case 0:
            print("Turning from grey to transparent BG, user is now prompted to swipe")
            
            MelodyTutorial.backgroundColor = UIColor(white: 0, alpha: 0.0)
            SwipePrompt.alpha = 1
            swipePromptArrow.alpha = 1
            MelodyImage.image = UIImage(named: "melLeft")
            SpeechLabel.text = "Swipe left to go to the next page."
            UIView.animate(withDuration: 1.5,
                           delay: 0.0,
                           options: .repeat,
                           animations: {
                            self.SwipePromptLeading.priority = UILayoutPriority(rawValue: 900)
                            self.view.layoutIfNeeded()
            },
                           completion: nil)
            melodyCounter += 1
            
        case 3:
            MelodyImage.image = UIImage(named: "melRight")
            SpeechLabel.text = "Tap on the cross at the top-right of the popup to close it."
            //MelodyTutorial.backgroundColor = UIColor(white: 0, alpha: 0.5)
            
            melodyCounter += 1
            
        default:
            print("You have fallen into the default switch case for TutorialViewTap")
            
        }
        
    }
    
    //This function runs when you swipe during the tutorial.
    @IBAction func TutorialViewSwipe(_ sender: UISwipeGestureRecognizer) {
        
        switch melodyCounter{
            
        case 1:
            // Animate out the old page
            UIView.animate(withDuration: 0.4,
                           delay: 0.0,
                           options: [.curveEaseOut],
                           animations: {
                            self.HTMLLeading.constant -= 1000
                            self.HTMLTrailing.constant -= 1000
                            self.view.layoutIfNeeded()
            }, completion: nil)
            
            // Change page after 0.3sec
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                self.nextpage(book: self.readingNow)
            }
            
            // Change position of HTML to the right of the screen
            UIView.animate(withDuration: 0.0,
                           delay: 0.4,
                           options: [.showHideTransitionViews],
                           animations: {
                            self.HTMLLeading.constant = 1000
                            self.HTMLTrailing.constant = 1000
                            self.view.layoutIfNeeded()},
                           completion: nil)
            
            // Animate in the new page
            UIView.animate(withDuration: 0.3,
                           delay: 0.4,
                           options: [.curveEaseOut],
                           animations: {
                            self.HTMLLeading.constant -= 1000
                            self.HTMLTrailing.constant -= 1000
                            self.view.layoutIfNeeded()
            }, completion: nil)
            
            print("User has swiped as prompted. User is now being prompted to click on highlighted word")
            SwipePrompt.removeFromSuperview()
            swipePromptArrow.removeFromSuperview()
            MelodyImage.image = UIImage(named: "melRight")
            SpeechLabel.text = "You can tap on highlighted words for an explanation!"
            melodyCounter += 1
            
            // Delay the appearance of the tapping prompt by 0.6s
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) {
                self.MelodyTutorial.backgroundColor = UIColor(white: 0, alpha: 0)
                self.topBlocker.alpha = 0.5
                self.leftBlocker.alpha = 0.5
                self.rightBlocker.alpha = 0.5
                self.botBlocker.alpha = 0.5
                self.TapPrompt.alpha = 1
                UIImageView.animate(withDuration: 1.5,
                                    delay: 0.0,
                                    options: .repeat,
                                    animations: {
                                        self.TapPromptTop.constant = -40
                                        self.view.layoutIfNeeded()
                },
                                    completion: nil)
            }
            
        default:
            print("You need to do something other than swipe.")
        }
    }
    
    //This function runs when you tap on the highlighted word.
    @IBAction func openPopup(_ sender: UITapGestureRecognizer) {
        switch melodyCounter{
            
        case 2:
            Popup.alpha = 1
            xPopup.alpha = 1
            melodyCounter += 1
            highlightWord.backgroundColor = UIColor(white: 0, alpha: 0.5)
            TapPrompt.removeFromSuperview()
            MelodyImage.image = UIImage(named: "melRightSmile")
            SpeechLabel.text = "Now you know the meaning of the word \"mermaid\"!"
            
        default:
            print("Please tap on the highlighted word")
        }
    }
    
    //This function runs when you close the pop-up.
    @IBAction func closePopup(_ sender: UIButton) {
        
        Popup.removeFromSuperview()
        xPopup.removeFromSuperview()
        MelodyImage.image = UIImage(named: "melLeftSmile")
        SpeechLabel.text = "Tap the icon on the bottom left to bookmark your progress and return to the library."
        
        // Animation for Melody to move to the bottom of the screen
        UIView.animate(withDuration: 1.5,
                       delay: 0.0,
                       options: .curveEaseOut,
                       animations: {
                        self.MelodyBubbleBot.constant = -10
                        self.view.layoutIfNeeded()
        },
                       completion: nil)
        
        libPromptArrow.alpha = 1.0
        UIView.animate(withDuration: 1.5,
                       delay: 0.0,
                       options: .repeat,
                       animations: {
                        self.LibPromptLeading.constant -= 40
                        self.view.layoutIfNeeded()},
                       completion: nil)
        
        bannerBlack.removeFromSuperview()
        melodyCounter = 6
    }
    
    //MARK: Storybook Functions
    
    //This function runs when you swipe left, i.e. you flip to the next page.
    @IBAction func leftswipepages(_ sender: UISwipeGestureRecognizer) {
        
        if readingNow.counter == readingNow.totalpages {
            return
        }
        
        else {
            // Animate out the old page
            UIView.animate(withDuration: 0.4,
                           delay: 0.0,
                           options: [.curveEaseOut],
                           animations: {
                            self.HTMLLeading.constant -= 1000
                            self.HTMLTrailing.constant -= 1000
                            self.view.layoutIfNeeded()
            }, completion: nil)
            
            // Change page after 0.3sec
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                self.nextpage(book: self.readingNow)
            }
            
            // Change position of HTML to the right of the screen
            UIView.animate(withDuration: 0.0,
                           delay: 0.4,
                           options: [.showHideTransitionViews],
                           animations: {
                            self.HTMLLeading.constant = 1000
                            self.HTMLTrailing.constant = 1000
                            self.view.layoutIfNeeded()},
                           completion: nil)
            
            // Animate in the new page
            UIView.animate(withDuration: 0.3,
                           delay: 0.4,
                           options: [.curveEaseOut],
                           animations: {
                            self.HTMLLeading.constant -= 1000
                            self.HTMLTrailing.constant -= 1000
                            self.view.layoutIfNeeded()
            }, completion: nil)
            
            // Music fades out for 1 second
            audioPlayer.setVolume(0, fadeDuration: 1)
            
            // Music player stops after 1 second, then starts.
            DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
                self.audioPlayer.stop()
                self.playSound(self.readingNow.songs[self.readingNow.counter], self.readingNow.songType)
                self.audioPlayer.setVolume(1, fadeDuration: 1)
            }
        }
    }
    
    // This function is run inside the function "leftswipepages"
    func nextpage(book: Book) {
        book.counter += 1
        if book.counter >= book.totalpages!{
            book.counter = book.totalpages!
            book.completion = true
            print (book.completion)
        }
        print("Counter: \(book.counter) , Page directory: \(book.pagedirectory), Page: \(book.page!)")
        tryloadingpages(book:book)
    }
    
    // This function runs when you swipe right, i.e. you flip to the previous page.
    @IBAction func rightswipepages(_ sender: UISwipeGestureRecognizer) {
        
        if readingNow.counter == 0 {
            return
        }
        
        else {
            // Animate out the old page
            UIView.animate(withDuration: 0.4,
                           delay: 0.0,
                           options: [.curveEaseOut],
                           animations: {
                            self.HTMLLeading.constant += 1000
                            self.HTMLTrailing.constant += 1000
                            self.view.layoutIfNeeded()
            }, completion: nil)
            
            // Go to previous page after 0.3sec
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                self.prevpage(book: self.readingNow)
            }
            
            // Change position of HTML to the right of the screen
            UIView.animate(withDuration: 0.0,
                           delay: 0.4,
                           options: [.showHideTransitionViews],
                           animations: {
                            self.HTMLLeading.constant = -1000
                            self.HTMLTrailing.constant = -1000
                            self.view.layoutIfNeeded()},
                           completion: nil)
            
            // Animate in the new page
            UIView.animate(withDuration: 0.3,
                           delay: 0.4,
                           options: [.curveEaseOut],
                           animations: {
                            self.HTMLLeading.constant += 1000
                            self.HTMLTrailing.constant += 1000
                            self.view.layoutIfNeeded()
            }, completion: nil)
            
            // Music fades out for 1 second
            audioPlayer.setVolume(0, fadeDuration: 1)
            
            // Music player stops after 1 second, then starts.
            DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
                self.audioPlayer.stop()
                self.playSound(self.readingNow.songs[self.readingNow.counter], self.readingNow.songType)
                self.audioPlayer.setVolume(1, fadeDuration: 1)
            }
        }
    }

    //This function is run inside the function "rightswipepages"
    func prevpage(book: Book) {
        book.counter -= 1
        if book.counter < 0{
            book.counter = 0
        }
        print("Counter: \(book.counter) , Page directory: \(book.pagedirectory), Page: \(book.page!)")
        tryloadingpages(book:book)
        return
    }
    
    //This function loads the pages, and is run inside the functions "nextpage" and "prevpage"
    func tryloadingpages(book: Book){
        print("Trying to load the page")
        
        //Book part
        book.pagedirectory = book.page! + String(book.counter)
        print("Page directory: \(book.pagedirectory)")
        
        do{
            guard let filePath = Bundle.main.path(forResource: book.pagedirectory, ofType: book.pageType)
                else {
                    print("Page file reading error")
                    return
            }
            htmlCode.load(URLRequest(url: URL(fileURLWithPath: filePath)))
        }
        pageNumber.text = "Page \(book.counter + 1) of \(book.totalpages! + 1)"
    }
    
    //MARK: Navigation
    
    //This function returns the user to the Library/Bookshelf
    @IBAction func goToLibrary(_ sender: UIButton) {
        
        let libraryPage = self.storyboard?.instantiateViewController(withIdentifier: "Librarypage") as! LibrarypageViewController
        
        if MelodyTutorialActive {
            
            //Change counter of selected book to counter before going to tutorial
            bookArray[selectedIndex].counter = originalpage
            
            //Update bookArray in Librarypage
            libraryPage.bookArray = bookArray
            print("Library page is updated from Storybook page")
            print("Bookarray in Library: \(libraryPage.bookArray)")
            
            //BGM Settings
            libraryPage.BGM = BGM!
            
            //Tutorial Settings
            libraryPage.TutorialCounter = TutorialCounter
            print("Tutorial counter: \(TutorialCounter)")
            
            //Stop music
            audioPlayer.stop()
            
            print("Going to Home")
            self.present(libraryPage, animated: true, completion: nil)
        }
        
        else {
            //Update current book
            bookArray[selectedIndex] = readingNow
            
            //Update bookArray in Librarypage
            libraryPage.bookArray = bookArray
            print("Library page is updated from Storybook page")
            print("Bookarray in Library: \(libraryPage.bookArray)")
            
            print("\(String(describing: libraryPage.bookArray[selectedIndex].name)) will continue from page \(libraryPage.bookArray[selectedIndex].counter + 1)")
            
            //BGM Settings
            libraryPage.BGM = BGM!
            
            //Tutorial Settings
            libraryPage.TutorialCounter = TutorialCounter
            print("Tutorial counter: \(TutorialCounter)")
            
            //Stop music
            audioPlayer.stop()
            
            print("Going to Home")
            self.present(libraryPage, animated: true, completion: nil)
        }
    }
    
    //MARK: Music Functions
    @IBOutlet weak var playButton: UIButton!
    var pauseInterval:TimeInterval = 0
    
    //The Play Music Button on the bottom right hand corner of the storybook.
    @IBAction func playButtonPress(_ sender: UIButton) {
        
        if pageBGM == false {
            
            if pauseInterval != 0{
                print("Audio was paused, it will now resume")
                audioPlayer.play()
                pauseInterval = 0
                pageBGM = true
                playButton.setBackgroundImage(UIImage(named: "Music On"), for: UIControlState.normal)
            }
            
            else{
                print("Playing music now")
                pageBGM = true
                playSound(readingNow.songs[readingNow.counter], readingNow.songType)
                playButton.setBackgroundImage(UIImage(named: "Music On"), for: UIControlState.normal)
            }
        }
        
        else {
            print("Pausing music now")
            pauseInterval = audioPlayer.currentTime
            print(pauseInterval)
            audioPlayer.pause()
            playButton.setBackgroundImage(UIImage(named: "Music Off"), for: UIControlState.normal)
            pageBGM = false
        }
    }
    
    /*The following function gets called when there is no BGM assigned to that page.
     This usually happens in the title page.
     */
    func playDefault(){
        
        guard let soundPath = Bundle.main.path(forResource: "BGM/RecordingNoSound", ofType: "wav") else {
            print("Error reading default sound file" )
            return
        }
        
        let soundURL = URL(fileURLWithPath: soundPath)
        
        //Trying to load and play the music
        do {
            audioPlayer = try AVAudioPlayer(contentsOf: soundURL)
            audioPlayer.numberOfLoops = -1
            //audioPlayer.setVolume(0, fadeDuration: 0)
            audioPlayer.prepareToPlay()
        }
            
        catch {
            print("Cannot load default player")
        }
        
        //Check if BGM is on
        if pageBGM! {
            print("pageBGM is true, now playing the default sound file with no sound.")
            audioPlayer.play()
        }
        else{
            print("pageBGM is false, not playing any sound file now.")
        }
    }
    
    //This function plays the music.
    func playSound(_ soundDirectory: String, _ soundType: String){
        
        //Music part
        pauseInterval = 0
        
        if readingNow.songs.count <= readingNow.counter{
            print("No songs to play, playing default sound which is no sound")
            playDefault()
        }
            
        else {
            //Finding the source of the sound file
            guard let soundPath = Bundle.main.path(forResource: soundDirectory, ofType: soundType)
                else {
                    print("Requested music file not found, will play default sound file with no sound")
                    playDefault()
                    return
            }
            
            let soundURL = URL(fileURLWithPath: soundPath)
            
            //Trying to load and play the music
            do {
                audioPlayer = try AVAudioPlayer(contentsOf: soundURL)
                audioPlayer.numberOfLoops = -1
                //audioPlayer.setVolume(1.0, fadeDuration: 2)
                audioPlayer.prepareToPlay()
            }
                
            catch {
                print("Cannot load player")
            }
            
            //Check if BGM is on
            if pageBGM! {
                print("pageBGM is true, so BGM will play.")
                audioPlayer.setVolume(0, fadeDuration: 0)
                audioPlayer.setVolume(1.0, fadeDuration: 1)
                audioPlayer.play()
            }
                
            else {
                print("pageBGM is not true, so BGM is not playing.")
            }
        }
    }
    
    //This button at the top-right quits the Tutorial prematurely.
    @IBAction func QuitTutorial(_ sender: UIButton) {
        let libraryPage = self.storyboard?.instantiateViewController(withIdentifier: "Librarypage") as! LibrarypageViewController
        
        //Change counter of selected book to counter before going to tutorial
        bookArray[selectedIndex].counter = originalpage
        
        //Update bookArray in Librarypage
        libraryPage.bookArray = bookArray
        print("Library page is updated from Storybook page")
        print("Bookarray in Library: \(libraryPage.bookArray)")
        
        //BGM Settings
        libraryPage.BGM = BGM!
        
        //Tutorial Settings
        libraryPage.TutorialCounter = TutorialCounter
        print("Tutorial counter: \(TutorialCounter)")
        melodyCounter = 0
        
        //Stop music
        audioPlayer.stop()
        
        print("Going to Home")
        self.present(libraryPage, animated: true, completion: nil)
    }
    
    //MARK: Initialization
    override func viewDidLoad() {
        super.viewDidLoad()
        
        print("Default BGM in Storybook page is \(BGM!)")
        
        //Default BGM settings
        if BGM == true {
            pageBGM = true
            playButton.setBackgroundImage(UIImage(named: "Music On"), for: UIControlState.normal)
        }
            
        else {
            pageBGM = false
            playButton.setBackgroundImage(UIImage(named: "Music Off"), for: UIControlState.normal)
        }
        
        //Load Music player
        playSound(readingNow.songs[readingNow.counter], readingNow.songType)
        
        //Load html page
        if readingNow.page != nil {
            tryloadingpages(book: readingNow)
        }
            
        else {
            print("Error in bringing book info from landing page")
        }
        
        //Load Tutorial
        if MelodyTutorialActive {
            print("Melody tutorial will load")
            MelodyTutorial.isHidden = false
        }
            
        else {
            print("Tutorial is not activated")
            MelodyTutorial.removeFromSuperview()
            bannerBlack.removeFromSuperview()
        }
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
