Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConditionSequence Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ConditionSequenceRef Class](topic12852.md) : GetConditionSequence Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    

Glossary Item Box

Gets the condition sequence from the specified project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetConditionSequence( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [Conditions](topic10865.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConditionSequenceRef](topic12852.md)
    Dim project As [Project](topic3859.md)
    Dim value As [Conditions](topic10865.md)
     
    value = instance.GetConditionSequence(project)  
  
C#|   
---|---  
      
    
    public abstract [Conditions](topic10865.md) GetConditionSequence( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConditionSequenceRef Class](topic12852.md)   
[ConditionSequenceRef Members](topic12853.md)


