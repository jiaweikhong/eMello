//
//  HomeViewController.swift
//  eMello
//
//  Created by eMelloTeam on 2018/6/5.
//  Copyright © 2018 testing. All rights reserved.
//

import UIKit
import CoreLocation
import CoreML
import CoreMedia

/* The Home View is the page where you are presented with two options: "Let's Start Reading!" and "Settings".
 */


class HomeViewController: UIViewController {
    
    //MARK: Properties
    var bookArray = [Book]() //bookArray refers to the list of books in the library - same across all viewcontrollers
    var BGM:Bool?
    var TutorialCounter = 0
    
    
    //MARK: Navigation
    
    //Go to Library a.k.a. Bookshelf
    @IBAction func goToLibrary(_ sender: Any) {
        let libraryPage = self.storyboard?.instantiateViewController(withIdentifier: "Librarypage") as! LibrarypageViewController
        
        //Update bookArray in Librarypage
        libraryPage.bookArray = bookArray
        print("Library page is updated from Home page")
        print("Bookarray in Library: \(libraryPage.bookArray)")
        
        //BGM Settings
        libraryPage.BGM = BGM
        
        //Tutorial Settings
        libraryPage.TutorialCounter = TutorialCounter
        print("Tutorial counter: \(TutorialCounter)")
        print("Going to Library")
        self.present(libraryPage, animated: true, completion: nil)
    }
    
    //Go to Settings
    @IBAction func goToSettings(_ sender: Any) {
        
        let settingsPage = self.storyboard?.instantiateViewController(withIdentifier: "SettingsPage") as! SettingsViewController
        
        //Update bookArray in Librarypage
        settingsPage.bookArray = bookArray
        print("Settings page is updated from Home page")
        print("Bookarray in Settings: \(settingsPage.bookArray)")
        
        //BGM Settings
        settingsPage.BGM = BGM
        
        //Tutorial Settings
        settingsPage.TutorialCounter = TutorialCounter
        print("Tutorial counter: \(TutorialCounter)")
        print("Going to Settings page")
        self.present(settingsPage, animated: true, completion: nil)
    }
    
    //MARK: Initialization
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if BGM == nil {
            BGM = true
        }
        print("Default BGM in Home page is \(BGM!)")
 
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
