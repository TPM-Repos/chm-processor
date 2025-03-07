Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DisplayHelpTopic Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : DisplayHelpTopic Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_topicName_
    The name of the help topic to show.

Glossary Item Box

Shows the specified help topic. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub DisplayHelpTopic( _
       ByVal _topicName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim topicName As String
     
    instance.DisplayHelpTopic(topicName)  
  
C#|   
---|---  
      
    
    protected virtual void DisplayHelpTopic( 
       string _topicName_
    )  
  
#### Parameters

 _topicName_
    The name of the help topic to show.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


