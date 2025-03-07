Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProcessPriorityOnly Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JobRequestTagInformation Class](topic3604.md) : ProcessPriorityOnly Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether tags other than the ones in the priority list can be processed but as a lower priority. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ProcessPriorityOnly As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JobRequestTagInformation](topic3604.md)
    Dim value As Boolean
     
    value = instance.ProcessPriorityOnly  
  
C#|   
---|---  
      
    
    public bool ProcessPriorityOnly {get;}  
  
# Remarks

True if we can only process the tags in the priority list, false if we can process any tags that aren't in the blocked list. By default this is False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JobRequestTagInformation Class](topic3604.md)   
[JobRequestTagInformation Members](topic3605.md)


