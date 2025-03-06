       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WithTransientEvent Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7725.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : WithTransientEvent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dynamicProperty_
    The property to which to attach the event.

_eventArg_
    The event details to include with changes to the property.

Glossary Item Box

Attaches the given event to the given property of the control so that changes to the property will include the event details, and returns an implementation of System.IDisposable that will detach when it is disposed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function WithTransientEvent( _
       ByVal _dynamicProperty_ As [DynamicProperty](topic9398.md), _
       ByVal _eventArg_ As [FormControlValueChangeEventArgs](topic2895.md) _
    ) As IDisposable  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim dynamicProperty As [DynamicProperty](topic9398.md)
    Dim eventArg As [FormControlValueChangeEventArgs](topic2895.md)
    Dim value As IDisposable
     
    value = instance.WithTransientEvent(dynamicProperty, eventArg)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public IDisposable WithTransientEvent( 
       [DynamicProperty](topic9398.md) _dynamicProperty_ ,
       [FormControlValueChangeEventArgs](topic2895.md) _eventArg_
    )  
  
#### Parameters

 _dynamicProperty_
    The property to which to attach the event.
_eventArg_
    The event details to include with changes to the property.

#### Return Value

An implementation of System.IDisposable that will detach when it is disposed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)

©2024 DriveWorks Ltd. All Rights Reserved.
