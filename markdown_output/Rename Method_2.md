       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Rename Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7717.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : Rename Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newName_
    The new name of the control.

Glossary Item Box

Renames the control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Sub Rename( _
       ByVal _newName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim newName As String
     
    instance.Rename(newName)  
  
C#|   
---|---  
      
    
    public virtual void Rename( 
       string _newName_
    )  
  
#### Parameters

 _newName_
    The new name of the control.

# Remarks

References to the renamed control are not refactored, to refactor them, use the [CreateRefactorProcess](topic7706.md) method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)

©2024 DriveWorks Ltd. All Rights Reserved.
