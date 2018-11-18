//
//  StartingPageViewController.swift
//  eMello
//
//  Created by eMelloTeam on 2018/7/26.
//  Copyright © 2018 testing. All rights reserved.
//

import UIKit
import os.log

/* The Starting Page refers to the page that the user first sees after pressing the App Icon.
 This is the page where the only option you have is to tap anywhere on the screen.
 */

class StartingPageViewController: UIViewController {
    
    //MARK: Properties
    @IBOutlet weak var TouchToBegin: UILabel!
    var bookArray = [Book]()
    
    //MARK: Actions
    @IBAction func goToHome(_ sender: UITapGestureRecognizer) {
        let homePage = self.storyboard?.instantiateViewController(withIdentifier: "HomePage") as! HomeViewController
        //Update bookArray in HomePage
        homePage.bookArray = bookArray
        print("Home now has book array from Start")
        print(homePage.bookArray)
        self.present(homePage, animated: true, completion: nil)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
