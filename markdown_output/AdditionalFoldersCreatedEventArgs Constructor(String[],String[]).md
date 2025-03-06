![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _relativePaths_() As String, _
       ByVal _fullPaths_() As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AdditionalFoldersCreatedEventArgs Class](topic10775.md)   
[AdditionalFoldersCreatedEventArgs Members](topic10776.md)   
[Overload List](topic10781.md)


