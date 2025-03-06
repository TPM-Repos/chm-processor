![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnMacroDialogClick Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [ProjectExtender Class](topic7232.md) : OnMacroDialogClick Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dialogButtonName_
    

Glossary Item Box

Called by DriveWorks when the DriveWorks_OnDialogClick macro is executed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnMacroDialogClick( _
       ByVal _dialogButtonName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectExtender](topic7232.md)
    Dim dialogButtonName As String
     
    instance.OnMacroDialogClick(dialogButtonName)  
  
C#|   
---|---  
      
    
    protected virtual void OnMacroDialogClick( 
       string _dialogButtonName_
    )  
  
#### Parameters

 _dialogButtonName_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectExtender Class](topic7232.md)   
[ProjectExtender Members](topic7233.md)


