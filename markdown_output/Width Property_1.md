       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Width Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : Width Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the width of the task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Property Width As Nullable(Of Double)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)
    Dim value As Nullable(Of Double)
     
    instance.Width = value
     
    value = instance.Width  
  
C#|   
---|---  
      
    
    public override Nullable<double> Width {get; set;}  
  
# Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The value is less than [DriveWorks.EventFlow.ExecutableNodeBase.MIN_WIDTH](topic6975.md) or greater than [DriveWorks.EventFlow.ExecutableNodeBase.MAX_WIDTH](topic6972.md).  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


