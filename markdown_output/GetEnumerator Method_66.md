Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowNodeCollection Class](topic7011.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an enumerator suitable for enumerating the nodes in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetEnumerator() As IEnumerator(Of ExecutableNodeBase)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowNodeCollection](topic7011.md)
    Dim value As IEnumerator(Of ExecutableNodeBase)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public abstract IEnumerator<ExecutableNodeBase> GetEnumerator()  
  
#### Return Value

An IEnumerator specialized for the [ExecutableNodeBase](topic6938.md) type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowNodeCollection Class](topic7011.md)   
[FlowNodeCollection Members](topic7012.md)


