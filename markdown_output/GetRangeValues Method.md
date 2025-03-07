Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRangeValues Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ExcelDocument Class](topic2834.md) : GetRangeValues Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all resolved values for ranges. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRangeValues() As Dictionary(Of String,String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExcelDocument](topic2834.md)
    Dim value As Dictionary(Of String,String)
     
    value = instance.GetRangeValues()  
  
C#|   
---|---  
      
    
    public Dictionary<string,string> GetRangeValues()  
  
#### Return Value

A dictionary where the key is the range name and the value is the resolved value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExcelDocument Class](topic2834.md)   
[ExcelDocument Members](topic2835.md)


