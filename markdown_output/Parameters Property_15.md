Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Parameters Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditionInfo Class](topic6536.md) : Parameters Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the collection of parameter info describing the rules of the condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Parameters As IEnumerable(Of ComponentTaskParameterInfo)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditionInfo](topic6536.md)
    Dim value As IEnumerable(Of ComponentTaskParameterInfo)
     
    value = instance.Parameters  
  
C#|   
---|---  
      
    
    public IEnumerable<ComponentTaskParameterInfo> Parameters {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskConditionInfo Class](topic6536.md)   
[ComponentTaskConditionInfo Members](topic6537.md)


