Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateRuleSearchProcess(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) > [CreateRuleSearchProcess Method](topic4906.md) : CreateRuleSearchProcess(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_searchString_
    The part of a rule to locate.

Glossary Item Box

Creates a new process capable of searching for parts of a rule in all rules in the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateRuleSearchProcess( _
       ByVal _searchString_ As String _
    ) As [RuleSearchProcess](topic13212.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim searchString As String
    Dim value As [RuleSearchProcess](topic13212.md)
     
    value = instance.CreateRuleSearchProcess(searchString)  
  
C#|   
---|---  
      
    
    public [RuleSearchProcess](topic13212.md) CreateRuleSearchProcess( 
       string _searchString_
    )  
  
#### Parameters

 _searchString_
    The part of a rule to locate.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)   
[Overload List](topic4906.md)


