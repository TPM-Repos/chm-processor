       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleTypes Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskParameterMetaData Class](topic6619.md) : RuleTypes Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the type the rule represents. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property RuleTypes As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskParameterMetaData](topic6619.md)
    Dim value() As String
     
    value = instance.RuleTypes  
  
C#|   
---|---  
      
    
    public string[] RuleTypes {get;}  
  
# Remarks

For a list of rule types see [DriveWorks.StandardRuleTypes](topic5461.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskParameterMetaData Class](topic6619.md)   
[ComponentTaskParameterMetaData Members](topic6620.md)


