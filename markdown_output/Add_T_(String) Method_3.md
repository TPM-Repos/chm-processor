_T_
    The type of the control to create.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add<T>(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) > [Add Method](topic7772.md) : Add<T>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the control to create.

Glossary Item Box

Creates and adds a new control with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add(Of T As [ControlBase](topic7698.md))( _
       ByVal _name_ As String _
    ) As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim name As String
    Dim value As T
     
    value = instance.Add(Of T)(name)  
  
C#|   
---|---  
      
    
    public T Add<T>( 
       string _name_
    )
    where T: [ControlBase](topic7698.md)  
  
#### Parameters

 _name_
    The name of the control to create.

#### Type Parameters

_T_
    The type of the control to create.

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


