Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FormatGeneratorFactory Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FormatGeneratorFactory Class](topic13670.md) : FormatGeneratorFactory Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_libraryManager_
    The library manager to use to discover different types of [FileFormatGenerator](topic13579.md).

Glossary Item Box

Creates a new instance of the [FormatGeneratorFactory](topic13670.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _libraryManager_ As [ILibraryManager](topic2079.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim libraryManager As [ILibraryManager](topic2079.md)
     
    Dim instance As New [FormatGeneratorFactory](topic13670.md)(libraryManager)  
  
C#|   
---|---  
      
    
    public FormatGeneratorFactory( 
       [ILibraryManager](topic2079.md) _libraryManager_
    )  
  
#### Parameters

 _libraryManager_
    The library manager to use to discover different types of [FileFormatGenerator](topic13579.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FormatGeneratorFactory Class](topic13670.md)   
[FormatGeneratorFactory Members](topic13671.md)


