       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateNamesInRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4925.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : UpdateNamesInRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleText_
    The rule in which to update names.

_nameMappings_
    An dictionary of mappings from old name to new name.

Glossary Item Box

Updates the names in the given rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function UpdateNamesInRule( _
       ByVal _ruleText_ As String, _
       ByVal _nameMappings_ As IDictionary(Of String,String) _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim ruleText As String
    Dim nameMappings As IDictionary(Of String,String)
    Dim value As String
     
    value = instance.UpdateNamesInRule(ruleText, nameMappings)  
  
C#|   
---|---  
      
    
    public string UpdateNamesInRule( 
       string _ruleText_ ,
       IDictionary<string,string> _nameMappings_
    )  
  
#### Parameters

 _ruleText_
    The rule in which to update names.
_nameMappings_
    An dictionary of mappings from old name to new name.

#### Return Value

The updated rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)

©2024 DriveWorks Ltd. All Rights Reserved.
