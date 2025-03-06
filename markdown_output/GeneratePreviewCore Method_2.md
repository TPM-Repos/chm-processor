![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GeneratePreviewCore Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3648.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JsonDocument Class](topic3635.md) : GeneratePreviewCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_previewDirectory_
    

_results_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Function GeneratePreviewCore( _
       ByVal _previewDirectory_ As String, _
       ByVal _results_ As [RuleResults](topic11136.md) _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [JsonDocument](topic3635.md)
    Dim previewDirectory As String
    Dim results As [RuleResults](topic11136.md)
    Dim value As String
     
    value = instance.GeneratePreviewCore(previewDirectory, results)  
  
C#|   
---|---  
      
    
    protected override string GeneratePreviewCore( 
       string _previewDirectory_ ,
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _previewDirectory_
    
_results_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[JsonDocument Class](topic3635.md)   
[JsonDocument Members](topic3636.md)

©2024 DriveWorks Ltd. All Rights Reserved.
