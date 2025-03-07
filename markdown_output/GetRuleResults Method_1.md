Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRuleResults Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JsonDocument Class](topic3635.md) : GetRuleResults Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a Dictionary of all Rule Ids for this document and their evaluated result. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRuleResults() As Dictionary(Of String,Object)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JsonDocument](topic3635.md)
    Dim value As Dictionary(Of String,Object)
     
    value = instance.GetRuleResults()  
  
C#|   
---|---  
      
    
    public Dictionary<string,object> GetRuleResults()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JsonDocument Class](topic3635.md)   
[JsonDocument Members](topic3636.md)


