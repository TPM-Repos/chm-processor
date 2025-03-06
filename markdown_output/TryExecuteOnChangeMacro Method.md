![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryExecuteOnChangeMacro Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7723.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : TryExecuteOnChangeMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    

_controlName_
    

_macroName_
    

_macroArgument_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub TryExecuteOnChangeMacro( _
       ByVal _e_ As [ValueChangedEventArgs](topic9575.md), _
       ByVal _controlName_ As String, _
       ByVal _macroName_ As String, _
       ByVal _macroArgument_ As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim e As [ValueChangedEventArgs](topic9575.md)
    Dim controlName As String
    Dim macroName As String
    Dim macroArgument As Object
     
    instance.TryExecuteOnChangeMacro(e, controlName, macroName, macroArgument)  
  
C#|   
---|---  
      
    
    protected void TryExecuteOnChangeMacro( 
       [ValueChangedEventArgs](topic9575.md) _e_ ,
       string _controlName_ ,
       string _macroName_ ,
       object _macroArgument_
    )  
  
#### Parameters

 _e_
    
_controlName_
    
_macroName_
    
_macroArgument_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)

©2024 DriveWorks Ltd. All Rights Reserved.
