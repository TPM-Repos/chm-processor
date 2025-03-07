Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ConditionRef Class](topic12843.md) : GetCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    

Glossary Item Box

Gets the condition from the specified project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetCondition( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [Condition](topic10804.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConditionRef](topic12843.md)
    Dim project As [Project](topic3859.md)
    Dim value As [Condition](topic10804.md)
     
    value = instance.GetCondition(project)  
  
C#|   
---|---  
      
    
    public [Condition](topic10804.md) GetCondition( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConditionRef Class](topic12843.md)   
[ConditionRef Members](topic12844.md)


