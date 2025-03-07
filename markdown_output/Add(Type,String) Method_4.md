Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(Type,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) > [Add Method](topic7772.md) : Add(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlType_
    The type of the control to create.

_name_
    The name of the control to create.

Glossary Item Box

Creates and adds a new control with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _controlType_ As Type, _
       ByVal _name_ As String _
    ) As [ControlBase](topic7698.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim controlType As Type
    Dim name As String
    Dim value As [ControlBase](topic7698.md)
     
    value = instance.Add(controlType, name)  
  
C#|   
---|---  
      
    
    public [ControlBase](topic7698.md) Add( 
       Type _controlType_ ,
       string _name_
    )  
  
#### Parameters

 _controlType_
    The type of the control to create.
_name_
    The name of the control to create.

#### Return Value

The new control.

# Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The specified type is either not the type of a control, or else isn't a valid child of the parent.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)   
[Overload List](topic7772.md)


