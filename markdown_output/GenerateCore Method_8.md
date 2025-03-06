![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerateCore Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4373.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) : GenerateCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_generateDirectory_
    The full path to the directory which generated files' paths should be created relative to.

_results_
    The calculated rule results for the document.

Glossary Item Box

When overridden in a derived class, generates the document. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Sub GenerateCore( _
       ByVal _generateDirectory_ As String, _
       ByVal _results_ As [RuleResults](topic11136.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim generateDirectory As String
    Dim results As [RuleResults](topic11136.md)
     
    instance.GenerateCore(generateDirectory, results)  
  
C#|   
---|---  
      
    
    protected abstract void GenerateCore( 
       string _generateDirectory_ ,
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _generateDirectory_
    The full path to the directory which generated files' paths should be created relative to.
_results_
    The calculated rule results for the document.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)

©2024 DriveWorks Ltd. All Rights Reserved.
