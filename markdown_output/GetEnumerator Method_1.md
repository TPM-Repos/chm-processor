Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an enumerator suitable for enumerating the operations in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of Operation)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim value As IEnumerator(Of Operation)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<Operation> GetEnumerator()  
  
#### Return Value

An IEnumerator specialized for the [Operation](topic11068.md) type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)


