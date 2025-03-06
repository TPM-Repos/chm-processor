![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetCheckedValue Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9276.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ToggleSwitch Class](topic9266.md) : SetCheckedValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The new value of the toggle switch control.

_eventArg_
    The arguments describing the source of this change.

Glossary Item Box

Sets the [ToggleSwitch](topic9266.md)'s [CheckedSourceProperty](topic9302.md) and temporarily registers the source of this change. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetCheckedValue( _
       ByVal _value_ As Object, _
       ByVal _eventArg_ As [FormControlValueChangeEventArgs](topic2895.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ToggleSwitch](topic9266.md)
    Dim value As Object
    Dim eventArg As [FormControlValueChangeEventArgs](topic2895.md)
     
    instance.SetCheckedValue(value, eventArg)  
  
C#|   
---|---  
      
    
    public void SetCheckedValue( 
       object _value_ ,
       [FormControlValueChangeEventArgs](topic2895.md) _eventArg_
    )  
  
#### Parameters

 _value_
    The new value of the toggle switch control.
_eventArg_
    The arguments describing the source of this change.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ToggleSwitch Class](topic9266.md)   
[ToggleSwitch Members](topic9267.md)

©2024 DriveWorks Ltd. All Rights Reserved.
