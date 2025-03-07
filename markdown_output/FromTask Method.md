Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ConditionSequenceRef Class](topic12852.md) : FromTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskRef_
    The reference to the task.

Glossary Item Box

Constructs a task sequence reference for the given event on the given state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromTask( _
       ByVal _taskRef_ As [TaskRef](topic13149.md) _
    ) As [ConditionSequenceRef](topic12852.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim taskRef As [TaskRef](topic13149.md)
    Dim value As [ConditionSequenceRef](topic12852.md)
     
    value = [ConditionSequenceRef](topic12852.md).FromTask(taskRef)  
  
C#|   
---|---  
      
    
    public static [ConditionSequenceRef](topic12852.md) FromTask( 
       [TaskRef](topic13149.md) _taskRef_
    )  
  
#### Parameters

 _taskRef_
    The reference to the task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConditionSequenceRef Class](topic12852.md)   
[ConditionSequenceRef Members](topic12853.md)


