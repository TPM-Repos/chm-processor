TryGetControl(String,ControlBase) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) > [TryGetControl Method](topic10240.md) : TryGetControl(String,ControlBase) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the control to get.

_control_
    The control.

Glossary Item Box

Gets a control given its name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetControl( _
       ByVal _name_ As String, _
       ByRef _control_ As [ControlBase](topic7698.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim name As String
    Dim control As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.TryGetControl(name, control)  
  
C#|   
---|---  
      
    
    public bool TryGetControl( 
       string _name_ ,
       ref [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _name_
    The name of the control to get.
_control_
    The control.

#### Return Value

True if the control was found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)   
[Overload List](topic10240.md)


