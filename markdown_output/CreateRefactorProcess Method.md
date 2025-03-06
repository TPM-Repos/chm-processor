![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateRefactorProcess Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7706.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : CreateRefactorProcess Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalName_
    

Glossary Item Box

Creates an object capable of refactoring all references to the control from its current name, to the given new name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Function CreateRefactorProcess( _
       ByVal _originalName_ As String _
    ) As [RenameProcess](topic10287.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim originalName As String
    Dim value As [RenameProcess](topic10287.md)
     
    value = instance.CreateRefactorProcess(originalName)  
  
C#|   
---|---  
      
    
    public virtual [RenameProcess](topic10287.md) CreateRefactorProcess( 
       string _originalName_
    )  
  
#### Parameters

 _originalName_
    

#### Return Value

A rename process.

# ![](dotnetimages/collapse.gif)Remarks

The returned RenameProcess instance is responsible for refactoring, only, it does not rename the control, for that, the [Rename](topic7717.md) method should be used.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)

©2024 DriveWorks Ltd. All Rights Reserved.
