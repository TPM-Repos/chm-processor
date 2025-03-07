Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LibraryEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [LibraryEventArgs Class](topic2124.md) : LibraryEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_libraryInfo_
    Information about the library that was loaded.

Glossary Item Box

Initializes a new instance of the [LibraryEventArgs](topic2124.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _libraryInfo_ As [ILibraryInfo](topic2055.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[LibraryEventArgs Class](topic2124.md)   
[LibraryEventArgs Members](topic2125.md)


