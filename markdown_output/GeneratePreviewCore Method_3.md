![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GeneratePreviewCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) : GeneratePreviewCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_previewDirectory_
    A fully-qualified path to a directory in which the preview file should be created.

_results_
    The calculated rule results for the document.

Glossary Item Box

When overridden in a derived class, generates a preview of the document in the specified directory using the given calculated rule results. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function GeneratePreviewCore( _
       ByVal _previewDirectory_ As String, _
       ByVal _results_ As [RuleResults](topic11136.md) _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim previewDirectory As String
    Dim results As [RuleResults](topic11136.md)
    Dim value As String
     
    value = instance.GeneratePreviewCore(previewDirectory, results)  
  
C#|   
---|---  
      
    
    protected virtual string GeneratePreviewCore( 
       string _previewDirectory_ ,
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _previewDirectory_
    A fully-qualified path to a directory in which the preview file should be created.
_results_
    The calculated rule results for the document.

#### Return Value

The full path to the preview file.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)


