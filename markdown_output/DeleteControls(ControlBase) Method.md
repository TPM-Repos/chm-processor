Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteControls(ControlBase) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [Form Class](topic8086.md) > [DeleteControls Method](topic8092.md) : DeleteControls(ControlBase) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control to delete.

Glossary Item Box

Deletes the specified control from the form. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function DeleteControls( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Form](topic8086.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.DeleteControls(control)  
  
C#|   
---|---  
      
    
    public bool DeleteControls( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The control to delete.

#### Return Value

True if the control was found and deleted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Form Class](topic8086.md)   
[Form Members](topic8087.md)   
[Overload List](topic8092.md)


