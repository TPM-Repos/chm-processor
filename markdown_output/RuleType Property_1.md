       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleType Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5974.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [IHasRuleType Interface](topic5969.md) : RuleType Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an array of type names which qualify the type of rule provided by the implementing class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property RuleType As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasRuleType](topic5969.md)
    Dim value() As String
     
    value = instance.RuleType  
  
C#|   
---|---  
      
    
    string[] RuleType {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasRuleType Interface](topic5969.md)   
[IHasRuleType Members](topic5970.md)

©2024 DriveWorks Ltd. All Rights Reserved.
