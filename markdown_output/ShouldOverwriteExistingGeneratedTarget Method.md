![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShouldOverwriteExistingGeneratedTarget Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15352.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Unified Namespace](topic15343.md) > [DiagnosticPreparationInteraction Class](topic15345.md) : ShouldOverwriteExistingGeneratedTarget Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_targetPath_
    The file-path of the existing generated file.

Glossary Item Box

Retrieves a saved 'Overwrite All' setting and/or prompts the user via a dialog as whether to overwrite the existing generated target. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ShouldOverwriteExistingGeneratedTarget( _
       ByVal _targetPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DiagnosticPreparationInteraction](topic15345.md)
    Dim targetPath As String
    Dim value As Boolean
     
    value = instance.ShouldOverwriteExistingGeneratedTarget(targetPath)  
  
C#|   
---|---  
      
    
    public bool ShouldOverwriteExistingGeneratedTarget( 
       string _targetPath_
    )  
  
#### Parameters

 _targetPath_
    The file-path of the existing generated file.

#### Return Value

True if the file should be overwritten, otherwise False.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DiagnosticPreparationInteraction Class](topic15345.md)   
[DiagnosticPreparationInteraction Members](topic15346.md)

©2024 DriveWorks Ltd. All Rights Reserved.
