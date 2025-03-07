Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetControl Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : GetControl Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the control to get.

Glossary Item Box

Gets a control given its name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetControl( _
       ByVal _name_ As String _
    ) As [ControlBase](topic7698.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim name As String
    Dim value As [ControlBase](topic7698.md)
     
    value = instance.GetControl(name)  
  
C#|   
---|---  
      
    
    public [ControlBase](topic7698.md) GetControl( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the control to get.

#### Return Value

The specified control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


