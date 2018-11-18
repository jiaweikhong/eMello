//
//  Book.swift
//  eMello
//
//  Created by eMelloTeam on 2018/6/28.
//  Copyright © 2018 testing. All rights reserved.
//

import Foundation

/* This class contains all the properties that a book should have.
 */

class Book {
    // MARK: Properties
    var imageName:String?
    var name:String?
    var totalpages:Int?
    var counter = 0
    var page:String?
    var pageType = ""
    var pagedirectory = ""
    var completion:Bool = false
    var songs = [String]()
    var songType = String()
}
