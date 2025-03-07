Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Conditions Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedComponentTask Class](topic5061.md) : Conditions Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the list of conditions that will be evaluated at runtime which governs whether the task will be executed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Conditions As IReadOnlyList(Of ReleasedComponentTaskCondition)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentTask](topic5061.md)
    Dim value As IReadOnlyList(Of ReleasedComponentTaskCondition)
     
    value = instance.Conditions  
  
C#|   
---|---  
      
    
    public IReadOnlyList<ReleasedComponentTaskCondition> Conditions {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentTask Class](topic5061.md)   
[ReleasedComponentTask Members](topic5062.md)


