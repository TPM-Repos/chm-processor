Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetVersionHistory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : GetVersionHistory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control to get the version history of.

Glossary Item Box

Returns the rule and comment history for given control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetVersionHistory( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As [RuleVersionDetails()](topic5277.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value() As [RuleVersionDetails](topic5277.md)
     
    value = instance.GetVersionHistory(control)  
  
C#|   
---|---  
      
    
    public [RuleVersionDetails[]](topic5277.md) GetVersionHistory( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The control to get the version history of.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)


