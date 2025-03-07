Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTopicName Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [HelpProvider Class](topic844.md) : GetTopicName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control to find the topic name on.

Glossary Item Box

Gets the topic name specified in the control or on the first visual parent of the control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetTopicName( _
       ByVal _control_ As DependencyObject _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim control As DependencyObject
    Dim value As String
     
    value = [HelpProvider](topic844.md).GetTopicName(control)  
  
C#|   
---|---  
      
    
    public static string GetTopicName( 
       DependencyObject _control_
    )  
  
#### Parameters

 _control_
    The control to find the topic name on.

#### Return Value

Topic name specified in the given control or one of its parents.

# Remarks

Returns nothing if no Topic name is specified in the visual tree.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[HelpProvider Class](topic844.md)   
[HelpProvider Members](topic845.md)


