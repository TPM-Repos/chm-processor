![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlValueChangedEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [ControlValueChangedEventArgs Class](topic9385.md) : ControlValueChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control that had a property change.

_dp_
    The property which has changed.

_oldValue_
    The value of the property before it was changed.

_newValue_
    The value of the property after it was changed.

_eventArg_
    The argument describing the source of this change.

Glossary Item Box

Initializes a new instance of the [ControlValueChangedEventArgs](topic9385.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _control_ As [ControlBase](topic7698.md), _
       ByVal _dp_ As [DynamicProperty](topic9398.md), _
       ByVal _oldValue_ As Object, _
       ByVal _newValue_ As Object, _
       ByVal _eventArg_ As [FormControlValueChangeEventArgs](topic2895.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim control As [ControlBase](topic7698.md)
    Dim dp As [DynamicProperty](topic9398.md)
    Dim oldValue As Object
    Dim newValue As Object
    Dim eventArg As [FormControlValueChangeEventArgs](topic2895.md)
     
    Dim instance As New [ControlValueChangedEventArgs](topic9385.md)(control, dp, oldValue, newValue, eventArg)  
  
C#|   
---|---  
      
    
    public ControlValueChangedEventArgs( 
       [ControlBase](topic7698.md) _control_ ,
       [DynamicProperty](topic9398.md) _dp_ ,
       object _oldValue_ ,
       object _newValue_ ,
       [FormControlValueChangeEventArgs](topic2895.md) _eventArg_
    )  
  
#### Parameters

 _control_
    The control that had a property change.
_dp_
    The property which has changed.
_oldValue_
    The value of the property before it was changed.
_newValue_
    The value of the property after it was changed.
_eventArg_
    The argument describing the source of this change.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlValueChangedEventArgs Class](topic9385.md)   
[ControlValueChangedEventArgs Members](topic9386.md)


