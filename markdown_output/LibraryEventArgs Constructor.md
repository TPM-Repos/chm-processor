![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LibraryEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2130.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [LibraryEventArgs Class](topic2124.md) : LibraryEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_libraryInfo_
    Information about the library that was loaded.

Glossary Item Box

Initializes a new instance of the [LibraryEventArgs](topic2124.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _libraryInfo_ As [ILibraryInfo](topic2055.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim libraryInfo As [ILibraryInfo](topic2055.md)
     
    Dim instance As New [LibraryEventArgs](topic2124.md)(libraryInfo)  
  
C#|   
---|---  
      
    
    public LibraryEventArgs( 
       [ILibraryInfo](topic2055.md) _libraryInfo_
    )  
  
#### Parameters

 _libraryInfo_
    Information about the library that was loaded.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[LibraryEventArgs Class](topic2124.md)   
[LibraryEventArgs Members](topic2125.md)

©2024 DriveWorks Ltd. All Rights Reserved.
