Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an enumerator suitable for enumerating the tasks in the task sequence. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of Task)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim value As IEnumerator(Of Task)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<Task> GetEnumerator()  
  
#### Return Value

An IEnumerator specialized for the [Task](topic11629.md) type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)


