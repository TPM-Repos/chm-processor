Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FailureMessages Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedTriggeredAction Class](topic5123.md) : FailureMessages Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets information regarding failed attempts at executing the triggered action. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property FailureMessages As IEnumerable(Of DeferredTaskFailureDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedTriggeredAction](topic5123.md)
    Dim value As IEnumerable(Of DeferredTaskFailureDetails)
     
    value = instance.FailureMessages  
  
C#|   
---|---  
      
    
    public IEnumerable<DeferredTaskFailureDetails> FailureMessages {get;}  
  
# Remarks

The size of this is limited to **MAX_FAIL_MESSAGE_COUNT**.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedTriggeredAction Class](topic5123.md)   
[ReleasedTriggeredAction Members](topic5124.md)


