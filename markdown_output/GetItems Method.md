Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetItems Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility Namespace](topic1277.md) > [IListPropertyEditor Interface](topic1291.md) : GetItems Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all item suggestions. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetItems() As IEnumerable(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IListPropertyEditor](topic1291.md)
    Dim value As IEnumerable(Of String)
     
    value = instance.GetItems()  
  
C#|   
---|---  
      
    
    IEnumerable<string> GetItems()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IListPropertyEditor Interface](topic1291.md)   
[IListPropertyEditor Members](topic1292.md)


