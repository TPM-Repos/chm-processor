Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRulesForPreview Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) > [IDocumentAdministrationController Interface](topic1509.md) : GetRulesForPreview Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a dictionary of rules ids and formulas for any rules which have been changed since the document administration was begun so that the preview capability can calculate the correct values. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetRulesForPreview() As IDictionary(Of String,String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDocumentAdministrationController](topic1509.md)
    Dim value As IDictionary(Of String,String)
     
    value = instance.GetRulesForPreview()  
  
C#|   
---|---  
      
    
    IDictionary<string,string> GetRulesForPreview()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDocumentAdministrationController Interface](topic1509.md)   
[IDocumentAdministrationController Members](topic1510.md)


