![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileFormatGenerationExceptionEventArgs Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [FileFormatGenerationExceptionEventArgs Class](topic15210.md) : FileFormatGenerationExceptionEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_targetPath_
    The target path.

_exception_
    The exception.

Glossary Item Box

Initializes a new instance of the [FileFormatGenerationExceptionEventArgs](topic15210.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _targetPath_ As String, _
       ByVal _exception_ As Exception _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim targetPath As String
    Dim exception As Exception
     
    Dim instance As New [FileFormatGenerationExceptionEventArgs](topic15210.md)(targetPath, exception)  
  
C#|   
---|---  
      
    
    public FileFormatGenerationExceptionEventArgs( 
       string _targetPath_ ,
       Exception _exception_
    )  
  
#### Parameters

 _targetPath_
    The target path.
_exception_
    The exception.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileFormatGenerationExceptionEventArgs Class](topic15210.md)   
[FileFormatGenerationExceptionEventArgs Members](topic15211.md)


