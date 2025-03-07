Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetColumns Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTable Class](topic3110.md) : GetColumns Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all columns present in this table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Function GetColumns() As IEnumerable(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTable](topic3110.md)
    Dim value As IEnumerable(Of String)
     
    value = instance.GetColumns()  
  
C#|   
---|---  
      
    
    public virtual IEnumerable<string> GetColumns()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupDataTable Class](topic3110.md)   
[GroupDataTable Members](topic3111.md)


