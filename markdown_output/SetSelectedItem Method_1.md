       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetSelectedItem Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8322.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ListControlBase Class](topic8315.md) : SetSelectedItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The new value of the control

_eventArg_
    The arguments describing the source of this change.

Glossary Item Box

Sets the [ListControlBase](topic8315.md)'s [SelectedItemSourceProperty](topic8339.md) and temporarily registers the source of this change. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetSelectedItem( _
       ByVal _value_ As Object, _
       ByVal _eventArg_ As [FormControlValueChangeEventArgs](topic2895.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ListControlBase](topic8315.md)
    Dim value As Object
    Dim eventArg As [FormControlValueChangeEventArgs](topic2895.md)
     
    instance.SetSelectedItem(value, eventArg)  
  
C#|   
---|---  
      
    
    public void SetSelectedItem( 
       object _value_ ,
       [FormControlValueChangeEventArgs](topic2895.md) _eventArg_
    )  
  
#### Parameters

 _value_
    The new value of the control
 _eventArg_
    The arguments describing the source of this change.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ListControlBase Class](topic8315.md)   
[ListControlBase Members](topic8316.md)

©2024 DriveWorks Ltd. All Rights Reserved.
