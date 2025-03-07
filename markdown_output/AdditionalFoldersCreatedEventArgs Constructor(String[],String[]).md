Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFoldersCreatedEventArgs Constructor(String[],String[])   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [AdditionalFoldersCreatedEventArgs Class](topic10775.md) > [AdditionalFoldersCreatedEventArgs Constructor](topic10781.md) : AdditionalFoldersCreatedEventArgs Constructor(String[],String[])  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_relativePaths_
    The relative paths of the additional folders that were created.

_fullPaths_
    The full paths of the additional folders that were created.

Glossary Item Box

Initializes a new instance of the [SpecificationDocumentEventArgs](topic11344.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _relativePaths_() As String, _
       ByVal _fullPaths_() As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim relativePaths() As String
    Dim fullPaths() As String
     
    Dim instance As New [AdditionalFoldersCreatedEventArgs](topic10775.md)(relativePaths, fullPaths)  
  
C#|   
---|---  
      
    
    public AdditionalFoldersCreatedEventArgs( 
       string[] _relativePaths_ ,
       string[] _fullPaths_
    )  
  
#### Parameters

 _relativePaths_
    The relative paths of the additional folders that were created.
_fullPaths_
    The full paths of the additional folders that were created.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AdditionalFoldersCreatedEventArgs Class](topic10775.md)   
[AdditionalFoldersCreatedEventArgs Members](topic10776.md)   
[Overload List](topic10781.md)


