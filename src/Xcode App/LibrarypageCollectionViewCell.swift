//
//  LibrarypageCollectionViewCell.swift
//  eMello
//
//  Created by eMelloTeam on 2018/6/28.
//  Copyright © 2018 testing. All rights reserved.
//

import UIKit

/* This class controls what goes on inside individual cells
 */

class LibrarypageCollectionViewCell: UICollectionViewCell {
    
    //MARK: BookCellProperties
    @IBOutlet weak var bookImage: UIImageView!
    @IBOutlet weak var bookName: UILabel!
    @IBOutlet weak var bookBackground: UIView!
    @IBOutlet weak var pageProgress: UIImageView!
    @IBOutlet weak var pageProgressText: UILabel!
    var book: Book?
    var gradient = CAGradientLayer()
    var colors = [CGColor]()
    var locations = [NSNumber]()
    
    //MARK: Gradient Function
    func createGradientLayer(_ colors:[CGColor],_ locations : [NSNumber]){
        print("creating gradient layer")
        gradient = CAGradientLayer()
        gradient.frame = self.bookBackground.bounds
        gradient.startPoint = CGPoint(x: 0.0, y: 0.5)
        gradient.endPoint = CGPoint(x: 1.0, y: 0.5)
        gradient.locations = locations
        gradient.colors = colors
        self.bookBackground.layer.addSublayer(gradient)
    }
    
    //MARK: Book cell layout functions
    func setBook(_ book:Book) {

        // Keep track of the book that gets passed in
        self.book = book
        
        //It display the book image if there is a book image
        if book.imageName != nil {
            bookImage.image = UIImage(named: book.imageName!)
            bookName.text = ""
            
            colors = [UIColor(red:255.0/255.0, green:255.0/255.0, blue:255.0/255.0, alpha:0.0).cgColor,
                      UIColor(red:0.0/255.0, green:0.0/255.0, blue:0.0/255.0, alpha:0.8).cgColor,
                      UIColor(red:0.0/255.0, green:0.0/255.0, blue:0.0/255.0, alpha:0.8).cgColor,
                      UIColor(red:255.0/255.0, green:255.0/255.0, blue:255.0/255.0, alpha:0.0).cgColor]
            
            locations = [0.0,0.2,0.8,1.0]
            
            createGradientLayer(colors, locations)
        }
        
        //If not it will display the book name
        else {
            bookName.text = book.name
            bookImage.image = UIImage(named: "Book holder")
            
            colors = [UIColor(red:255.0/255.0, green:255.0/255.0, blue:255.0/255.0, alpha:0.0).cgColor,
                      UIColor(red:0.0/255.0, green:0.0/255.0, blue:0.0/255.0, alpha:0.8).cgColor,
                      UIColor(red:0.0/255.0, green:0.0/255.0, blue:0.0/255.0, alpha:0.8).cgColor,
                      UIColor(red:255.0/255.0, green:255.0/255.0, blue:255.0/255.0, alpha:0.0).cgColor]
            
            locations = [0.0,0.1,0.9,1.0]
            
            createGradientLayer(colors, locations)
        }
        
        //The following codes displays the current reading status of the book
        if book.completion {
            pageProgress.image = UIImage(named: "Green")
            pageProgressText.text = "Read Again"
            book.counter = 0
            book.completion = false
        }
        
        else if book.counter != 0{
            pageProgress.image = UIImage(named: "Purple")
            pageProgressText.text = "Continue from page \(book.counter + 1)"
        }
        
        else{
            pageProgress.image = UIImage(named: "Purple")
            pageProgressText.text = "Start Reading"
        }
        
        //This will display the upload function of our application
        if book.imageName == "Book plus" {
            bookName.text = ""
            colors = [UIColor(red:255.0/255.0, green:255.0/255.0, blue:255.0/255.0, alpha:0.0).cgColor,
                      UIColor(red:0.0/255.0, green:0.0/255.0, blue:0.0/255.0, alpha:0.8).cgColor,
                      UIColor(red:0.0/255.0, green:0.0/255.0, blue:0.0/255.0, alpha:0.8).cgColor,
                      UIColor(red:255.0/255.0, green:255.0/255.0, blue:255.0/255.0, alpha:0.0).cgColor]
            locations = [0.0,0.2,0.8,1.0]
            createGradientLayer(colors, locations)
            pageProgress.image = UIImage(named: "Purple")
            pageProgressText.text = "Upload"
        }
    }
}
