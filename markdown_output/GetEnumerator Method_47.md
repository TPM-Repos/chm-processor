Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Columns Class](topic2516.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns an enumerator that iterates through the [Columns](topic2516.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of Column)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Columns](topic2516.md)
    Dim value As IEnumerator(Of Column)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<Column> GetEnumerator()  
  
#### Return Value

An enumerator that iterates through the [Columns](topic2516.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Columns Class](topic2516.md)   
[Columns Members](topic2517.md)


