Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [FlowPropertyData Class](topic12873.md) : FromTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task containing the properties to copy.

Glossary Item Box

Gets an array of [FlowPropertyData](topic12873.md) instances for the given task's properties. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromTask( _
       ByVal _task_ As [Task](topic11629.md) _
    ) As [FlowPropertyData()](topic12873.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim task As [Task](topic11629.md)
    Dim value() As [FlowPropertyData](topic12873.md)
     
    value = [FlowPropertyData](topic12873.md).FromTask(task)  
  
C#|   
---|---  
      
    
    public static [FlowPropertyData[]](topic12873.md) FromTask( 
       [Task](topic11629.md) _task_
    )  
  
#### Parameters

 _task_
    The task containing the properties to copy.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowPropertyData Class](topic12873.md)   
[FlowPropertyData Members](topic12874.md)


